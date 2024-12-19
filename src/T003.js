import React, { useState } from "react";
import { useNavigate, useLocation } from "react-router-dom";
import "./T003.css";
import Header, { handleMakePlanClick } from "./template.js";

function T003() {
    const navigate = useNavigate();
    const location = useLocation();

    const items = [
        { id: "f001", name: "自然" },
        { id: "f002", name: "体験" },
        { id: "f003", name: "春" },
        { id: "f004", name: "夏" },
        { id: "f005", name: "秋" },
        { id: "f006", name: "冬" },
        { id: "f091", name: "工科大学生おすすめ", tag: "KUT" }
    ];

    const spotData = location.state?.spotDatas;
    const MainSpotID = location.state?.mainSpotID;

    const [filteredIDs, setFilteredIDs] = useState([]); // 現在選択されているフィルタID
    const [filterType, setFilterType] = useState("or");
    const [filteredDatas, setFilteredDatas] = useState([]); // フィルタリング結果
    const [mainSpotID, setMainSpotID] = useState(MainSpotID); // メインスポット
    const [filterIDs, setFilterID] = useState([]);

    // 今日の日付を取得してISO形式（YYYY-MM-DD）に変換
    const today = new Date().toISOString().split("T")[0];

    const [travelStart, setTravelStart] = useState(today);
    const [travelEnd, setTravelEnd] = useState(today);

    const handleSelectMainSpotChange = (event) => {
        setMainSpotID(event.target.value); // 選択した値を状態に設定
    };

    const handleSelectFilterTypeChange = (event) => {
        setFilterType(event.target.value); // 選択した値を状態に設定
    };

    const setFilterIDtoBar = (filterID) => {
        // 現在のfilterIDsを基に新しい配列を作成してfilterIDを追加する
        setFilterID(prevFilterIDs => [...prevFilterIDs, filterID]);
    };

    const handleSelectTravelStartChange = (event) => {
        setTravelStart(event.target.value); // 選択した値を状態に設定
    };

    const handleSelectTravelEndChange = (event) => {
        setTravelEnd(event.target.value); // 選択した値を状態に設定
    };

    const handleMakePlan = () => {
        console.log("メインスポットID:", mainSpotID);
        console.log("フィルタ:", filterIDs);
        console.log("フィルタタイプ:", filterType);
        console.log("開始日:", travelStart);
        console.log("終了日:", travelEnd);
    }
    return (
        <div>
            <Header />
            <div className="select-main-spot">
                <h3>メインスポット</h3>
                <label>
                    <select
                        className="spots"
                        value={mainSpotID}
                        onChange={handleSelectMainSpotChange} // 値が変更されたら状態を更新
                    >
                        {spotData.data.map((spot, index) => (
                            <option key={index} value={spot.spot_id}>
                                {spot.name}
                            </option>
                        ))}
                    </select>
                </label>
            </div>
            {/* フィルタバー */}
            <div className="filter">
                <h3>スポットフィルタ</h3>
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
            </div>
            <div className="travel-date">
                <h3>日程</h3>
                <p>旅行開始日</p>
                <input
                    type="date"
                    id="travel-start"
                    value={travelStart}
                    onChange={handleSelectTravelStartChange}
                />
                <p>旅行終了日</p>
                <input
                    type="date"
                    id="travel-end"
                    value={travelEnd}
                    onChange={handleSelectTravelEndChange}
                />
            </div>
            <div className="make-plan">
                <button
                    className="make-plan-button"
                    onClick={() => handleMakePlanClick({
                        mainSpotID: mainSpotID,
                        inputData: spotData,
                        filterType: filterType,
                        inputFilterIDs: filterIDs,
                        inputTravelStart: travelStart,
                        inputTravelEnd: travelEnd
                    })}
                >
                    プランを作成
                </button>
            </div>
        </div>
    );
}

export default T003;