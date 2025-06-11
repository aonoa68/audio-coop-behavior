# audio-coop-behavior
音声刺激を用いた協力行動および経済ゲームに関する心理実験プログラムです。| Scripts for psychological experiments on cooperative behavior and economic games using audio stimuli.

## 概要（Overview）

本リポジトリは、協力行動（cooperative behavior）と経済ゲーム（economic games）を音声刺激を通じて研究するための心理実験用スクリプトを公開しています。

## 実験の目的（Experimental Purpose）

音声を用いて地域やアクセント、イントネーションが協力行動や信頼関係の構築に与える影響を検証することを目的としています。

## 使用技術（Technologies Used）

- Python 3.x
- Pygame
- Numpy
- wxPython（使用する場合のみ）

## ファイル構成（File Structure）
audio-coop-behavior/
├── audio/ # 音声刺激ファイル（wav形式）
├── faceshuffle/ # 提示用画像ファイル（png形式）
├── fonts/ # フォントファイル（ipag.ttfなど）
└── test07.py # 実験用Pythonスクリプト


## セットアップ方法（Setup & Installation）

必要なライブラリを以下のコマンドでインストールします：

pip install pygame numpy wxpython


フォントファイルは各自で取得し、`fonts/`フォルダ内に置いてください。

## 実行方法（Usage）

次のコマンドで実行します：

python test07.py


事前に音声ファイルと画像ファイルを指定フォルダに配置する必要があります。

## 実験手順（Procedure）

1. プログラム起動後、提示される指示に従います。
2. 音声刺激および画像刺激が順番に提示されます。
3. 被験者の応答（キー入力など）を記録します。
4. 結果データはファイルに記録されます。

## ライセンス（License）

このプロジェクトは[MIT License](LICENSE)で公開されています。

## 著者（Author）

- 氏名：小野原彩香
