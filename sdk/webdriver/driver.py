"""Chrome を起動し、待機付きで操作する。

要素は既定で XPath で指定する。`by` に `By.CSS_SELECTOR` などを渡せば別の指定方法も使える。
ドライバ（chromedriver）は Selenium 4.6 以上に入っている Selenium Manager が用意する。
"""

import logging
import time
from types import TracebackType

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logger = logging.getLogger(__name__)


class WebDriverSession:
    """Chrome を 1 つ起動し、待機付きの操作メソッドを持つ。

    `with` で使うと、抜けるときに Chrome を閉じる。
    Selenium の WebDriver そのものは `driver` で取れる。
    """

    def __init__(
        self,
        download_dir: str | None = None,
        *,
        headless: bool = True,
        wait_timeout: float = 20,
        page_load_timeout: float = 600,
    ) -> None:
        self._wait_timeout = wait_timeout
        options = Options()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        if download_dir:
            options.add_experimental_option(
                "prefs",
                {
                    "download.default_directory": download_dir,
                    "download.prompt_for_download": False,
                },
            )
        self._driver: WebDriver = Chrome(options=options)
        self._driver.set_page_load_timeout(page_load_timeout)
        logger.debug("Chrome を起動しました（headless=%s）", headless)

    def __enter__(self) -> "WebDriverSession":
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        self.quit()

    @property
    def driver(self) -> WebDriver:
        return self._driver

    def quit(self) -> None:
        self._driver.quit()

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    def get(self, url: str, *, seconds: float = 1) -> None:
        """`url` を開き、`seconds` 秒待つ。"""
        self._driver.get(url)
        time.sleep(seconds)

    def save_screenshot(self, path: str) -> bool:
        return self._driver.save_screenshot(path)

    def _wait(self, condition, selector: str, by: str) -> WebElement:
        return WebDriverWait(self._driver, self._wait_timeout).until(
            condition((by, selector))
        )

    def wait_present(self, selector: str, by: str = By.XPATH) -> WebElement:
        """要素が DOM に現れるまで待つ。"""
        return self._wait(EC.presence_of_element_located, selector, by)

    def wait_clickable(self, selector: str, by: str = By.XPATH) -> WebElement:
        """要素がクリックできるようになるまで待つ。"""
        return self._wait(EC.element_to_be_clickable, selector, by)

    def wait_visible(self, selector: str, by: str = By.XPATH) -> WebElement:
        """要素が見えるようになるまで待つ。"""
        return self._wait(EC.visibility_of_element_located, selector, by)

    def get_text(self, selector: str, by: str = By.XPATH) -> str:
        """要素が見えるまで待ち、前後の空白を除いた文字列を返す。"""
        return self.wait_visible(selector, by).text.strip()

    def get_attribute(self, selector: str, name: str, by: str = By.XPATH) -> str | None:
        return self.wait_present(selector, by).get_attribute(name)

    def is_present(self, selector: str, by: str = By.XPATH, *, timeout: float = 0) -> bool:
        """要素があれば True。`timeout` 秒まで待つ（既定は待たない）。"""
        if timeout <= 0:
            return bool(self._driver.find_elements(by, selector))
        try:
            WebDriverWait(self._driver, timeout).until(
                EC.presence_of_element_located((by, selector))
            )
            return True
        except Exception:
            return False

    def find_elements(self, selector: str, by: str = By.XPATH) -> list[WebElement]:
        """待たずに、今ある要素をすべて返す（無ければ空のリスト）。"""
        return self._driver.find_elements(by, selector)

    def find_element(self, selector: str, by: str = By.XPATH) -> WebElement:
        return self.wait_present(selector, by)

    def click(self, selector: str, by: str = By.XPATH) -> None:
        """クリックできるようになるまで待ってクリックする。"""
        self.wait_clickable(selector, by).click()

    def send_keys(
        self, selector: str, text: str, by: str = By.XPATH, *, clear: bool = True
    ) -> None:
        """入力欄が見えるまで待ち、`text` を入れる。既定では先に中身を消す。"""
        element = self.wait_visible(selector, by)
        if clear:
            element.clear()
        element.send_keys(text)
