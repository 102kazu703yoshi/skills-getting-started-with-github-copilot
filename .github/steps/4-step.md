## Step 4: Planning Agent で実装を計画する 🧭

前の Step では、Agent Mode のおかげで速く動き、新しい機能を出せました。 🚀

今度は 1 回だけ速度を落として、設計者のように進めます。まずしっかりしたテスト方針を決めてから、実装に渡します。計画を先に立てると見通しがよくなり、想定外が減り、結果もきれいになります。 🧪

### 📖 理論: Copilot Plan Agent とは

Copilot の [Plan Agent](https://code.visualstudio.com/docs/copilot/agents/planning) は、コードを変更する前に解決策を設計する手助けをします。

いきなり編集を始めるのではなく、依頼内容を調べ、確認の質問をし、練り直せる実装計画を書き出します。

#### Plan Agent の要点

| 観点 | 🧭 Plan Agent |
| --- | --- |
| 目的 | コーディングを始める前に、構造化された実装計画を作ります。 |
| コンテキストの収集 | 読み取り専用の調査で、要件と制約を理解します。 |
| 進め方 | 確認の質問をし、答えを使って計画を更新します。 |
| 繰り返し | 実装前に何度でも計画を練り直せます。 |
| 安全性 | 計画を承認して **Agent Mode** に引き渡すまで、ファイルを編集しません。 |
| 引き渡し | **Start implementation** ボタンで、承認した計画を **Agent Mode** に渡してコーディングを始めます。 |

> [!TIP]
> 大まかな依頼から始めて、後続のプロンプトで制約や詳細を足していけます。

### ⌨️ やること: バックエンドのテストを計画して実装する

バックエンドにはまだテストがまったくありません。**Plan Agent** で計画を作り、質問に答えて、実装を開始しましょう。

1. **Copilot Chat** パネルを開き、**Plan Agent** に切り替えます。

   <img width="350" alt="image" src="../images/plan-mode-dropdown.png" />


1. まずは大まかなプロンプトから始めます。細かいところは Copilot が埋めるのを手伝ってくれます。

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Let's plan for adding backend FastAPI tests in a separate tests directory.
   > ```

1. Copilot が最初の計画を作るまで待ちます。質問されたら、できる範囲で答えてください。 

   > 🪧 **注:** 完璧を目指さなくて構いません。計画は後から練り直せます。

1. 後続のプロンプトで、計画を練り直したり詳細を足したりできます。

   例を示します。

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Let's use the AAA (Arrange-Act-Assert) testing pattern to structure our tests
   > ```

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Make sure we use `pytest` and add it to `requirements.txt` file
   > ```


1. 提案された計画を確認し、納得できたら **Start implementation** をクリックして **Agent Mode** に引き渡します。

   <img width="350" alt="image" src="../images/plan-mode-start-implementation.png" />

   ボタンを押すと **Plan** から **Agent Mode** に切り替わったことに注目してください。切り替わったあとは、前の Step と同じように Copilot がコードベースを編集できます。

1. 作った計画を Copilot が実装していく様子を見ます。ツールの実行（コマンドの実行や仮想環境の作成など）の許可を求められることがあります。作業を続けられるよう承認してください。

1. 変更を確認し、テストが正常に実行されることを確かめます。必要なら、実装が終わるまで指示を続けてください。

   **🎯 目標: 先へ進む前に、すべてのテストを通す（緑にする）こと。 ✅**

   > 🪧 **注:** Agent Mode は 1 回で終えることもあれば、追加のプロンプトが必要なこともあります。

1. すべての変更を `accelerate-with-copilot` ブランチに **Commit** して **push** します。

1. Mona が作業を確認しています。少し待って、コメントを見てください。進捗と次の Step が投稿されます。

<details>
<summary>うまくいかないとき 🤷</summary><br/>

- テストが実行されなかった場合は、実行するよう Copilot に頼んでください。
- `requirements.txt` に `pytest` が追加され、`tests/` ディレクトリがあることを確認してください。

</details>
