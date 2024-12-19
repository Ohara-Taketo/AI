import React, { useState } from "react";
import { useNavigate, useLocation } from "react-router-dom";
import "./T002.css";
import Header, { handleFilterClick } from "./template.js";

function T002() {
    const navigate = useNavigate();
    const location = useLocation();

    const items = [
        { id: "f001", name: "自然" },
        { id: "f002", name: "体験" },
        { id: "f003", name: "春" },
        { id: "f004", name: "夏" },
        { id: "f005", name: "秋" },
        { id: "f006", name: "冬" },
        { id: "f091", name: "工科大学生おすすめTOP3", tag: "KUT" }
    ];

    // 渡されたデータを取得
    const spotData = location.state?.spotDatas;
    const Query = location.state?.query;
    const FilteredIDs = location.state?.filteredIDs;
    const FilteredDatas = location.state?.filteredDatas;

    const [query, setQuery] = useState(Query); // 検索ワード
    const [filteredIDs, setFilteredIDs] = useState(FilteredIDs); // 現在選択されているフィルタID
    const [filterType, setFilterType] = useState("or");
    const [filteredDatas, setFilteredDatas] = useState(FilteredDatas); // フィルタリング結果
    const [mainSpot, setMainSpot] = useState(""); // メインスポット
    const [filterIDs, setFilterID] = useState(FilteredIDs);

    const handleSelectFilterTypeChange = (event) => {
        setFilterType(event.target.value); // 選択した値を状態に設定
    };

    const setFilterIDtoBar = (filterID) => {
        // 現在のfilterIDsを基に新しい配列を作成してfilterIDを追加する
        setFilterID(prevFilterIDs => [...prevFilterIDs, filterID]);
    };

    return (
        <div>
            <Header />

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
                    onClick={() => {
                        setFilterID([]);
                        handleFilterClick({
                            path: "/T002",
                            inputData: spotData,
                            filterMode: "search",
                            inputText: query,
                            setQuery,
                            setFilteredIDs,
                            setFilteredDatas,
                            navigate
                        })
                    }}
                >
                    検索
                </button>
            </div>

            {/* フィルタバー */}
            <div className="filter-bar">
                <div className="selected-filter-ids">
                    {items
                        .filter((item) => filterIDs.includes(item.id)) // filterIDsに含まれるオブジェクトを抽出
                        .map((item) => (
                            <div key={item.id} className="filter-item">
                                {item.name}
                                <button
                                    className="remove-button"
                                    onClick={() => setFilterID((prev) => prev.filter((id) => id !== item.id))}
                                >
                                    ×
                                </button>
                            </div>
                        ))}
                </div>
                <label>
                    <select
                        className="filter-type"
                        value={filterType} // 現在の状態を選択ボックスに反映
                        onChange={handleSelectFilterTypeChange} // 値が変更されたら状態を更新
                    >
                        <option value="or">OR</option>
                        <option value="and">AND</option>
                    </select>
                </label>

                {/* ボタンでフィルタを適用 */}
                <button
                    className="filter-button"
                    onClick={() => {
                        // 数値部分が90以上のフィルタIDを抽出
                        const above90FilterIDs = filterIDs.filter(
                            (id) => Number(id.substring(1, 4)) >= 90
                        );

                        // 条件によって異なる動作を実行
                        if (above90FilterIDs.length === 0) {
                            handleFilterClick({
                                path: "/T002",
                                inputData: spotData,
                                filterMode: "filter",
                                filterType: filterType,
                                inputFilterIDs: filterIDs,
                                setQuery,
                                setFilteredIDs,
                                setFilteredDatas,
                                navigate,
                            });
                        } else {
                            // above90FilterIDsを除いた新しいリストを作成
                            const removeAbove90FilterIDs = filterIDs.filter(
                                (id) => !above90FilterIDs.includes(id)
                            );
                            // その最初のIDに一致するオブジェクトのtagを取得
                            const sortKey =
                                above90FilterIDs.length > 0
                                    ? items.find((item) => item.id === above90FilterIDs[0])?.tag || "a"
                                    : "KUT";
                            handleFilterClick({
                                path: "/T002",
                                inputData: spotData,
                                filterMode: "filter",
                                filterType: filterType,
                                inputFilterIDs: removeAbove90FilterIDs,
                                sortKey: sortKey,
                                limitNumber: 3,
                                setQuery,
                                setFilteredIDs,
                                setFilteredDatas,
                                navigate,
                            });
                        }
                    }}
                >
                    フ
                </button>
            </div>

            <div className="T002-horizontal-scroll">
                {items.map((item) => (
                    <div
                        key={item.id}
                        className="T002-scroll-item"
                        onClick={() => setFilterIDtoBar(item.id)}
                    >
                        {item.name}
                    </div>
                ))}
            </div>

            {/* データが存在する場合の表示 */}
            <div className="filter-result">
                {FilteredDatas.data.length > 0 ? (
                    <div>
                        <h3>フィルタリングされた観光地</h3>
                        <ul>
                            {FilteredDatas.data.map((item, index) => (
                                <li key={index}>{item.name}</li>
                            ))}
                        </ul>
                    </div>
                ) : (
                    <p className="no-data">データがありません</p>
                )}
            </div>
        </div>
    );
}

export default T002;

