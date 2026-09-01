## Step 2: Copilot で作業を進める

前の Step では、GitHub Copilot にプロジェクトの内容を教えてもらいました。説明を受けるだけでも大きな時間短縮ですが、次は実際の作業をしてみましょう。

:bug: **ウェブサイトにバグがあります** :bug:

申し込みの流れにおかしいところが見つかりました。
生徒が同じ活動に **2 回以上**申し込めてしまいます。原因を突き止め、きれいな修正の形にするところまで、Copilot がどこまでやってくれるか見てみましょう。

始める前に、Copilot の仕組みを簡単に押さえます。 🧑‍🚀

### 📖 理論: Copilot の仕組み

ひとことで言うと、Copilot はとても専門性の高い同僚だと考えられます。うまく働いてもらうには、背景（コンテキスト）と、はっきりした指示（プロンプト）を渡す必要があります。さらに、人によって経験や得意なことが違うように、Copilot にも複数のモデルがあります。

- **どうやってコンテキストを渡す？:** 開発環境の中では、Copilot は近くのコードと開いているタブを自動的に見ています。チャットを使う場合は、ファイルを明示的に指定することもできます。

- **どのモデルを選ぶ？:** 演習ではあまり気にしなくて構いません。いろいろなモデルを試すのも楽しみのひとつです。モデル選びはまた別のレッスンで。 🤖

- **プロンプトはどう書く？:** はっきりと具体的に書くほど、Copilot はよい仕事をします。ただし従来の仕組みと違って、後から追加のプロンプトで指示を補うことができます。

> [!TIP]
> Copilot の知識と能力を補う方法は他にもあります。[chat participants](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/github-copilot-chat-cheat-sheet?tool=vscode#chat-participants)、[chat variables](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/github-copilot-chat-cheat-sheet?tool=vscode#chat-variables)、[slash commands](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/github-copilot-chat-cheat-sheet?tool=vscode#slash-commands-1)、[MCP tools](https://code.visualstudio.com/docs/copilot/chat/mcp-servers) などです。

### :keyboard: やること: Copilot で申し込みのバグを直す :bug:

1. バグの原因がどこにありそうか、Copilot に聞いてみましょう。**Copilot Chat** パネルを **Ask mode** で開き、次を入力します。

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > #codebase Students are able to register twice for an activity.
   > Where could this bug be coming from?
   > ```

1. 問題が `src/app.py` ファイルの `signup_for_activity` メソッドにあるとわかったので、Copilot のすすめに従って直しに行きます（半分手作業で行います）。まずコメントを書き、続きは Copilot に埋めてもらいます。
   1. `src/app.py` ファイルを開きます。

      > 💡 **ヒント:** Copilot がチャットの中で `src/app.py` に触れている場合は、チャットビューでファイル名を直接クリックして開けます。

   1. ファイルの下のほうにある `signup_for_activity` 関数を探します。

   1. 生徒を追加する処理を説明しているコメント行を探します。コメント行の上が、申し込み済みかどうかの確認を入れるのに自然な場所です。

   1. 次のコメントを入力して Enter を押し、次の行へ移ります。少し待つと、Copilot の候補が薄い文字（シャドーテキスト）で表示されます。 :tada:

      コメント:

      ```python
      # Validate student is not already signed up
      ```

      <img width="700" alt="Copilot shadow text suggestion in the editor" src="../images/shadow-text.gif" />

   1. `Tab` を押して Copilot の候補を受け入れ、シャドーテキストをコードに変えます。

   <details>
   <summary>Example Results</summary><br/>

   Copilot は日々成長していて、いつも同じ結果になるとは限りません。候補が気に入らない場合のために、演習を作ったときに得られた正しい候補の例を載せておきます。例を使って先に進んでも構いません。

   ```python
   @app.post("/activities/{activity_name}/signup")
   def signup_for_activity(activity_name: str, email: str):
      """Sign up a student for an activity"""
      # Validate activity exists
      if activity_name not in activities:
         raise HTTPException(status_code=404, detail="Activity not found")

      # Get the activity
      activity = activities[activity_name]

      # Validate student is not already signed up
      if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student is already signed up")

      # Add student
      activity["participants"].append(email)
      return {"message": f"Signed up {email} for {activity_name}"}
   ```

   </details>

### :keyboard: やること: Copilot にサンプルデータを作ってもらう 📋

新しいプロジェクトの開発では、テスト用に本物らしい架空のデータがあると便利なことがよくあります。Copilot はサンプル作りがとても得意なので、課外活動のサンプルをもう少し追加してみましょう。あわせて、**Inline Chat** という別のやり取りの方法も使います。

**Inline Chat** と **Copilot Chat** パネルは似ていますが、扱う範囲が違います。Copilot Chat は複数ファイルにまたがる質問や、調べながらの質問に向いています。Inline Chat は、目の前の 1 行やかたまりについて的を絞って助けてほしいときのほうが速いです。

1. `src/app.py` ファイルの上のほう（23 行目あたり）にある `activities` 変数を探します。サンプルの課外活動が設定されています。

1. `activities` 辞書の全体を、上から下へマウスでドラッグして選択します。選択すると、次のプロンプトのためのコンテキストを Copilot に渡せます。

   <img width="700" alt="Highlighted activities dictionary before opening inline chat" src="../images/activities-dict-highlighted.png" />


1. キーボードの `Ctrl + I`（Windows）または `Cmd + I`（Mac）で Copilot の Inline Chat を開きます。

   > 💡 **ヒント:** 選択した行のどこかを `右クリック` → `Open Inline Chat` でも Inline Chat を開けます。

1. 次のプロンプトを入力し、Enter を押すか右側の **Send** ボタンを押します。

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Add 2 more sports related activities, 2 more artistic
   > activities, and 2 more intellectual activities.
   > ```

1. 少し待つと、Copilot がコードを直接書き換え始めます。追加と削除がひと目でわかるように、変更部分は違う見た目で表示されます。変更を確かめてから、**Keep** ボタンを押します。

   <details>
   <summary>Example Results</summary><br/>

   Copilot は日々成長していて、いつも同じ結果になるとは限りません。候補が気に入らない場合のために、演習を作ったときに得られた結果の例を載せておきます。うまくいかないときは、例を使って先に進んでも構いません。

   ```python
   # In-memory activity database
   activities = {
      "Chess Club": {
         "description": "Learn strategies and compete in chess tournaments",
         "schedule": "Fridays, 3:30 PM - 5:00 PM",
         "max_participants": 12,
         "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
      },
      "Programming Class": {
         "description": "Learn programming fundamentals and build software projects",
         "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
         "max_participants": 20,
         "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
      },
      "Gym Class": {
         "description": "Physical education and sports activities",
         "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
         "max_participants": 30,
         "participants": ["john@mergington.edu", "olivia@mergington.edu"]
      },
      "Basketball Team": {
         "description": "Competitive basketball training and games",
         "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
         "max_participants": 15,
         "participants": []
      },
      "Swimming Club": {
         "description": "Swimming training and water sports",
         "schedule": "Mondays and Wednesdays, 3:30 PM - 5:00 PM",
         "max_participants": 20,
         "participants": []
      },
      "Art Studio": {
         "description": "Express creativity through painting and drawing",
         "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
         "max_participants": 15,
         "participants": []
      },
      "Drama Club": {
         "description": "Theater arts and performance training",
         "schedule": "Tuesdays, 4:00 PM - 6:00 PM",
         "max_participants": 25,
         "participants": []
      },
      "Debate Team": {
         "description": "Learn public speaking and argumentation skills",
         "schedule": "Thursdays, 3:30 PM - 5:00 PM",
         "max_participants": 16,
         "participants": []
      },
      "Science Club": {
         "description": "Hands-on experiments and scientific exploration",
         "schedule": "Fridays, 3:30 PM - 5:00 PM",
         "max_participants": 20,
         "participants": []
      }
   }
   ```

   </details>

1. ウェブサイトを開いて、新しい活動が表示されていることを確認できます。

### :keyboard: やること: 作業内容の説明を Copilot に書いてもらう 💬

バグを直し、サンプルの活動を増やせました。次は、作業をコミットして GitHub に push します。今回も Copilot に手伝ってもらいましょう。

1. 左のサイドバーで `Source Control` タブを選びます。

   > 💡 **ヒント:** ソース管理の場所からファイルを開くと、単に開くのではなく元との差分が表示されます。

1. `app.py` ファイルを探し、`+` を押して変更をステージング領域にまとめます。

   ![image](../images/staging-changes-icon.png)

1. ステージした変更の一覧の上にある **Message** の入力欄を見つけます。ただし、今は**何も入力しないでください**。
   - ふだんは入力欄に変更内容の短い説明を書きますが、今回は Copilot に手伝ってもらいます。

1. **Message** 入力欄の右にある **Generate Commit Message** ボタン（きらきらのアイコン）を見つけてクリックします。

1. **Commit** ボタンと **Sync Changes** ボタンを押して、変更を GitHub に push します。

1. Mona が作業を確認しています。少し待って、コメントを見てください。進捗と次の Step が投稿されます。

<details>
<summary>うまくいかないとき 🤷</summary><br/>

反応がないときは、次を確認してください。

- `src/app.py` の変更を、`accelerate-with-copilot` ブランチに push したか。

</details>
