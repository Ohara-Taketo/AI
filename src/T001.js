// モジュール内で複数の特定の名前を持つエクスポートがある場合、名前付きエクスポートされる
// その場合、{}で囲む
import React, { useState } from "react";
// FastAPIを利用するためインポートする
import axios from "axios";
// ページ遷移に必要
import { useNavigate, useLocation } from "react-router-dom";
// 見た目の設定ファイル
import "./T001.css";
import Header, { handleFilterClick, selectMainSpot } from "./template.js";

// アロー関数
// この方法はモダンなReactアプリケーションで広く使われており、簡潔で直感的にコンポーネントを定義できる
// 画面の表示に必要なデータや処理を集めたものをコンポーネントといい、Reactでは、コンポーネントは大文字で始める
const T001 = () => {
    // 「useNavigate」はフック
    // Reactにおいてフックとは、開発者がクラスコンポーネントを必要とせずにReactのstateやその他の機能を使用できるようにする特別な機能
    // ループ、条件分岐、ネストされた関数、try/catch/finallyブロックの内部でフックを呼び出してはならない
    // フックは常にReact関数のトップレベルで、早期returnを行う前に呼び出す
    // フックは状態管理やライフサイクルを扱うことができる
    // フックを使用すればクラスコンポーネントでできていたことが、関数コンポーネントでもできる
    // クラスコンポーネントは、Reactの古典的な方法で、JavaScriptのクラスを使って定義される
    // クラスコンポーネントでは、「render」メソッドを用いてUIを返す
    // 関数コンポーネントは、よりシンプルで簡潔な構文でコンポーネントを定義できる
    // 通常、アロー関数を使って定義され、UIを直接返す
    // とりあえず、「useNavigate」はフックというもので、下記のようにしないとコードが動かない
    const navigate = useNavigate();
    const location = useLocation();

    // 条件絞り込みについてのjsonっぽい情報
    // jsonではない
    const items = [
        { id: "f001", name: "自然", path: "/T002" },
        { id: "f002", name: "体験", path: "/T002" },
        { id: "f003", name: "春", path: "/T002" },
        { id: "f004", name: "夏", path: "/T002" },
        { id: "f005", name: "秋", path: "/T002" },
        { id: "f006", name: "冬", path: "/T002" },
        { id: "f091", name: "工科大学生おすすめTOP3", path: "/T002", tag: "KUT" }
    ];

    // 渡されたデータを取得
    // 「location.state?.filteredDatas」のように書くことで、「state」や「filteredDatas」が未定義の場合でもエラーを回避できる
    const spotData = location.state?.spotDatas;
    const Query = location.state?.query;
    const FilteredIDs = location.state?.filteredIDs;
    const FilteredDatas = location.state?.filteredDatas;

    // ページが初期化されると、「data」は「useState(初期値)」の「初期値」となる
    // ボタンをクリックすると、「setData(新しいデータ)」が呼ばれ、「data」に「新しいデータ」が設定される
    // 状態が更新されると、Reactが自動的に再レンダリングを行い、画面に「新しいデータ」が表示される
    // 下記では現在の状態の値を入れる変数名を「query」、状態を更新する関数を「setQuery」と名付け、「query」の初期値を「""」としただけ
    // Reactのフックである「useState」を使って、状態(state)を定義している
    // 「query」は現在の状態の値、読み取り専用で値を直接変更することはできない
    // 「setQuery」は状態を更新するための関数、新しい値を渡すと、Reactが再レンダリングをトリガーしてUIを更新する
    // 「useState(null)」は初期値を「null」と設定している
    // 「useState()」は初期値を「undefined」と設定している
    const [query, setQuery] = useState(Query); // 検索ワード
    const [filteredIDs, setFilteredIDs] = useState(FilteredIDs); // 現在選択されているフィルタID
    const [filteredDatas, setFilteredDatas] = useState(FilteredDatas); // フィルタリング結果
    const [mainSpotID, setMainSpotID] = useState(""); // メインスポット
    const [isPopupVisible, setPopupVisible] = useState(false);
    const [popupContent, setPopupContent] = useState("");

    // 関数
    const handleItemClick = (index) => {
        setPopupContent(filteredDatas.data[index]); // クリックしたアイテムの内容を設定
        setPopupVisible(true); // ポップアップを表示
    };

    const closePopup = () => {
        setPopupVisible(false); // ポップアップを非表示
        setPopupContent(""); // 内容をクリア
    };


    return (
        <div>
            {/* ヘッド */}
            {/* <div>はコンテンツ区分要素 */}
            {/* ヘッド部分をテンプレート化 */}
            <Header />

            {/* 機能名 */}
            <div className="function-name">
                <h2>AIトラベル</h2>
            </div>

            {/* 検索バー */}
            <div className="search-bar">
                <input
                    type="text"
                    id="search-input"
                    placeholder="検索..."
                    value={query}
                    onChange={(e) => setQuery(e.target.value)} // 入力の状態を管理
                    className="search-input"
                />
                <button
                    className="search-button"
                    onClick={() => handleFilterClick({
                        path: "/T002",
                        inputData: spotData,
                        filterMode: "search",
                        inputText: query,
                        setQuery,
                        setFilteredIDs,
                        setFilteredDatas,
                        navigate
                    })
                    }
                >
                    検索
                </button>
            </div>

            {/* 条件で探す */}
            <div className="search-content">
                <h3>条件で探す</h3>
            </div>

            {/* 横スクロールエリア */}
            <div className="horizontal-scroll">
                {/* map関数とは配列やオブジェクトを取り出して繰り返し処理を行うJavaScriptのメソッド */}
                {/* 「items」の各要素に対し、繰り返し処理を行う */}
                {/* 「item」が横並びで配置されるのはcssのおかげ */}
                {/* jsxでjavascriptのコードを埋め込むには「{}」で囲む */}
                {items.map((item) => (
                    <div
                        key={item.id}
                        className="scroll-item"
                        onClick={() =>
                        (Number(item.id.substring(1, 4)) <= 90
                            ? handleFilterClick({
                                path: item.path,
                                inputData: spotData,
                                filterMode: "filter",
                                inputFilterIDs: [item.id],
                                setQuery,
                                setFilteredIDs,
                                setFilteredDatas,
                                navigate,
                            })
                            : handleFilterClick({
                                path: item.path,
                                inputData: spotData,
                                sortKey: item.tag,
                                limitNumber: 3,
                                setQuery,
                                setFilteredIDs,
                                setFilteredDatas,
                                navigate
                            })
                        )
                        }
                    >
                        {/* key属性は、Reactがリストや配列をレンダリングするときに、それぞれの要素を一意に識別するために使用される */}
                        {item.name}
                    </div>
                ))}
            </div>

            {/* 工科大生のイチオシ! */}
            <div className="recommend-content">
                {FilteredDatas.data.length > 0 ? (
                    <div>
                        <h3>高知工科大学生のイチオシ!</h3>
                        <ul>
                            {FilteredDatas.data.map((item, index) => (
                                <li
                                    key={index}
                                    onClick={() => handleItemClick(index)} // クリック時にポップアップを表示
                                    className="clickable-item"
                                >
                                    No{index + 1}. {item.name}
                                </li>
                            ))}
                        </ul>
                    </div>
                ) : (
                    <p className="no-data">データがありません</p>
                )}

                {/* ポップアップの実装 */}
                {isPopupVisible && (
                    <div className="popup-overlay" onClick={closePopup}>
                        {/* 背景のクリック可能部分をクリックしても反応しないようにする */}
                        <div className="popup-content" onClick={(e) => e.stopPropagation()}>
                            <p>{popupContent.name}</p>
                            <img src={popupContent.image_path} alt={popupContent.name} />
                            <div className="popup-btn">
                                <button className="close-btn" onClick={closePopup}>
                                    閉じる
                                </button>
                                <button className="close-btn" onClick={() => selectMainSpot({
                                    path: "/T003",
                                    inputData: spotData,
                                    spotData: popupContent,
                                    setMainSpotID,
                                    navigate
                                })}>
                                    メ追加
                                </button>
                            </div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default T001;
