"""業務の流れ。画面やファイルの読み書きは components に任せ、ここからは呼ぶだけにする。

ブラウザ・保存先・logger は impl から受け取る。
流れが増えたら example.py をコピーして 1 流れ 1 ファイルにし、`{流れの名前}UseCase` クラスをここで公開する。
"""

from usecases.example import ExampleUseCase

__all__ = ["ExampleUseCase"]
