## Step 3: Copilot Agent Mode を使う 🚀

### 📖 理論: Copilot Agent Mode とは

Copilot の [agent mode](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode) は、AI 支援コーディングの次の段階です。自律的な相棒プログラマーとして、指示に応じて複数の手順にわたるコーディング作業を行います。

Copilot Agent Mode は、コンパイルエラーや lint エラーに反応し、ターミナルやテストの出力を見ながら、作業が終わるまで自動で修正を繰り返します。

#### Agent Mode の要点

| 観点 | 👩‍🚀 Agent Mode |
| --- | --- |
| 自律性と計画 | ざっくりした依頼を複数の手順に分解し、作業が終わるまで繰り返します。 |
| コンテキストの収集 | 今のコンテキストを使い、必要なら関連するファイルを自分で見つけられます。 |
| ツールの利用 | 使うツールを自動で選んで呼び出します。`#codebase` のような書き方でツールを指定することもできます。 |
| 承認と安全のための確認 | 影響の大きい操作は、実行前に承認を求める設定にできます。主導権を保てます。 |

#### 🧰 Agent Mode のツール

Agent Mode は、依頼を処理する中で専門的な作業を行うためにツールを使います。たとえば次のような作業です。

- プロンプトを実行するのに必要なファイルを探す
- ウェブページの内容を取得する
- テストやターミナルのコマンドを実行する

> [!TIP]
> VS Code には多くの組み込みツールがありますが、**MCP tools** を通じて Agent Mode に分野固有の能力を追加することもできます。
>
> 詳しくは [MCP servers](https://code.visualstudio.com/docs/copilot/customization/mcp-servers) と [GitHub MCP Server](https://github.com/github/github-mcp-server) を参照してください。

では **Agent Mode** を試してみましょう。 👩‍🚀

### :keyboard: やること: Copilot で新しい機能を追加する :rocket:

ウェブサイトは活動を一覧表示していますが、参加者は伏せられたままです。 🤫 

Copilot を使って、各活動の下に申し込み済みの生徒を表示するように変えてみましょう。

1. Copilot Chat ウィンドウの下部にあるドロップダウンで、**Agent** モードに切り替えます。

   <img width="350" alt="image" src="../images/agent-mode-dropdown.png" />

1. ウェブページに関係するファイルを開き、各エディターウィンドウ（またはファイル）をチャットパネルへドラッグして、コンテキストとして使うよう Copilot に伝えます。

   - `src/static/app.js`
   - `src/static/index.html`
   - `src/static/styles.css`

   > 🪧 **注:** ファイルをコンテキストに追加するのは任意です。追加しなくても、Copilot Agent Mode は `#codebase` などのツールを使って、プロンプトから関連ファイルを探せます。ファイルを指定すると Copilot を正しい方向へ導きやすくなり、特に大きなコードベースで役立ちます。

   <img width="400" alt="image showing files added to context" src="../images/files-added-to-context.png" />

   > 💡 **ヒント:** **Add Context...** ボタンを使うと、GitHub の issue やターミナルウィンドウの結果など、他の情報もコンテキストとして渡せます。

1. 活動の現在の参加者を表示するようにプロジェクトを更新してほしい、と Copilot に頼みます。編集の提案が届いて適用されるまで少し待ちます。

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Hey Copilot, can you please edit the activity cards to add a participants section.
   > It will show what participants that are already signed up for that activity as a bulleted list.
   > Remember to make it pretty!
   > ```

   Copilot が作業を終えたあと、どの変更を残すかは自分で決めます。 

   下の **Keep** ボタンを使って、すべての変更をまとめて受け入れる／破棄する、または 1 件ずつ確認して決める、のどちらもできます。チャットパネルからでも、編集された各ファイルを見ながらでも操作できます。

      <img width="900" alt="buttons to keep or discard changes" src="../images/review-changes-buttons.png" />


1. すぐに変更を受け入れる前に、もう一度ウェブサイトを見て、想定どおりに更新されているか確認してください。
   
   更新後の活動カードの例を示します。アプリの再起動やページの再読み込みが必要なことがあります。

   <img width="350" alt="Activity card with participant info" src="../images/activity-card-with-participants.png" />

   > 🪧 **注:** 活動カードの見た目は違うかもしれません。Copilot はいつも同じ結果を出すとは限りません。

   <details>
   <summary>うまくいかないとき 🤷</summary><br/>
   ウェブサイトが読み込まれないときは、次を確認してください。

   - VS Code のデバッガーを再起動し、最新版のサイトが配信されているようにする。
   - URL を忘れた、ウィンドウを閉じてしまった場合は、Step 1 を見直す。
   - ページをハード再読み込みするか、プライベートウィンドウで開いて、新しいコピーを取得してみる。

   </details>

1. 変更が問題ないと確認できたら、パネルで提案された編集を 1 つずつ確認し、**Keep** を押して適用します。

   > 💡 **ヒント:** 提案された変更を受け入れる、手で直す、チャットで追加の指示を出して調整する、のいずれもできます。

### :keyboard: やること: Agent モードで「登録解除」ボタンを動くように追加する

もう少し自由度の高い依頼を試して、ウェブアプリに機能を足してみましょう。

思ったとおりの結果にならない場合は、別のモデルを試したり、追加のフィードバックを出して結果を調整したりできます。

1. Copilot が **Agent** モードのままであることを確認します。

   <img width="250" alt="agent mode" src="../images/agent-mode-dropdown.png" />

1. **Tools** アイコンをクリックして、いま Copilot Agent Mode が使えるツールを一通り見てみます。

   <img width="250"  alt="tools icon" src="../images/tools-icon.png" />

1. 試してみましょう。参加者を削除する機能を追加するよう Copilot に頼みます。

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > #codebase Please add a delete icon next to each participant and hide the bullet points.
   > When clicked, it will unregister that participant from the activity.
   > ```

   `#codebase` ツールは、いまの作業に関係するファイルやコードのかたまりを Copilot が探すために使います。

   > 🪧 **注:** 演習では、結果をなるべく同じにするために `#codebase` ツールを明示的に指定しています。
   > `#codebase` を**付けずに**同じプロンプトを試して、Agent Mode が自分でプロジェクト全体のコンテキストを集めるかどうかを見てみるのもよいでしょう。

1. Copilot が終わったら、コードの変更とウェブサイト上の結果を確認します。結果が気に入ったら **Keep** ボタンを押します。気に入らなければ、Copilot にフィードバックを返して調整してみてください。

   > 🪧 **注:** ウェブサイトに変更が反映されない場合は、デバッガーの再起動が必要なことがあります。

1. 申し込みのバグを直すよう Copilot に頼みます。

   > 💡 **ヒント:** 申し込みの流れを自分でも試しておくと、前後の動きの違いがはっきりわかります。

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > I've noticed there seems to be a bug.
   > When a participant is registered, the page must be refreshed to see the change on the activity.
   > ```

1. Copilot が終わったら、結果を確認し、ウェブサイト上で申し込みの流れを検証します。

   結果が気に入ったら **Keep** ボタンを押します。気に入らなければ、Copilot にフィードバックを返してみてください。

1. すべての変更を `accelerate-with-copilot` ブランチに **Commit** して **push** します。

1. Mona が作業を確認しています。少し待って、コメントを見てください。進捗と次の Step が投稿されます。