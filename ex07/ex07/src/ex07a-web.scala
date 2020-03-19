/*
 * Copyright (c) 2011-2014, ScalaFX Project
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *     * Redistributions of source code must retain the above copyright
 *       notice, this list of conditions and the following disclaimer.
 *     * Redistributions in binary form must reproduce the above copyright
 *       notice, this list of conditions and the following disclaimer in the
 *       documentation and/or other materials provided with the distribution.
 *     * Neither the name of the ScalaFX Project nor the
 *       names of its contributors may be used to endorse or promote products
 *       derived from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL THE SCALAFX PROJECT OR ITS CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED
 * AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

/* 上の著作権規定の概略
 * 以下のコードは ScalaFX プロジェクトに著作権が帰属しています．
 * コードをそのまま，あるいは改変して再配布をすることは以下の条件をみたす場合にのみこれを許します．
 *  1. 上記の著作権表記と使用条件を保持すること
 *  2. バイナリ形式での配布のための条件
 *  3. このコードに由来する製品の販売促進を目的として ScalaFX プロジェクトの名前を使用してはいけない．
 */

package nobita4.ex07a

import scalafx.Includes._
import scalafx.application.JFXApp
import scalafx.application.JFXApp.PrimaryStage
import scalafx.event.ActionEvent
import scalafx.scene.Scene
import scalafx.scene.control._
import scalafx.scene.layout._
import scalafx.scene.web._
import scalafx.scene.paint.Color
import scalafx.beans.property

object WebDemo extends JFXApp {

  val homepage = "http://www.is.titech.ac.jp/"
  var history:List[String]=List()
  var current_index:Int=0
  
  def onBrowserStatusChanged() {

  }
  def onPrevPage() {
    
  }

  def onNextPage() {
   
  }
  val browser = new WebView {
    hgrow = Priority.Always
    vgrow = Priority.Always

    onStatusChanged = handle { onBrowserStatusChanged() }
  }

  val engine = browser.engine
  engine.load(homepage)
  history=history:+homepage//homepageを追加

  val txfUrl = new TextField {
    text = engine.location.value
    hgrow = Priority.Always
    vgrow = Priority.Never
    onAction = handle{ engine.load(this.text.get) }
  }

  val btnHome = new Button("ホーム") {
    onAction = handle { engine.load(homepage) }
  }

  val btnHistory = new Button("履歴") {
    onAction = handle { onHistory() }
  }

  def onHistory() {}

  // btnPrevPage と btnNextPage に閲覧履歴の機能を付加したい．閲覧履歴はどのように記憶すればいいだろうか？また，閲覧履歴へのアクセスはどのように行うべきだろうか？コードを書く前に状態を扱うためのデザインレシピに沿って分析をすること．
  val btnPrevPage = new Button("前のページ") { onAction = onPrevPage _ }
  val btnNextPage = new Button("次のページ") { onAction = onNextPage _ }

  

  val btnAddToFavorite = new Button("☆")    { onAction = onAddToFavorite _ }
  val mnuFavorite = new MenuButton("お気に入り")
  def addFavoriteMenuItem(title: String, url: String) {
    val item = new MenuItem(title) {
      onAction = handle { engine.load(url) }
    }

    mnuFavorite.items += item

    // 以上で，メニュー項目をメニューに登録できました．
    // さて，URLはどのように記憶するばいいでしょう？
  }

  addFavoriteMenuItem("東工大",     "http://www.titech.ac.jp")
  addFavoriteMenuItem("情報科学科", "http://www.is.titech.ac.jp")
  addFavoriteMenuItem("脇田研究室", "http://kwakita.wordpress.com/")

  def onAddToFavorite(e: ActionEvent) {

    val title=engine.title.value
    val url=engine.location.value
    
    mnuFavorite.items foreach{m_item=>
      if(m_item.text.value==title){
          mnuFavorite.items.remove(m_item)
          return
        }
    }
      addFavoriteMenuItem(title,url)
  }
  
  
  
  def onSelectFavorite(title: String, e: ActionEvent) {
    println("お気に入りを選ぼうとしています")
  }

  stage = new PrimaryStage {
    title = "ScalaFX Web Demo"
    width = 800
    height = 600
    scene = new Scene {
      fill = Color.LightGray
      root = new BorderPane {
        hgrow = Priority.Always
        vgrow = Priority.Always
        top = new HBox {
          content = List(btnHome, btnPrevPage, btnNextPage, txfUrl, btnAddToFavorite, mnuFavorite)
        }
        center = browser
      }
    }
  }

}
