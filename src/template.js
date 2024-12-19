import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import "./template.css";

// フィルタリング機能を呼び出すのに必要なURL
const url_filter = "http://127.0.0.1:8000/run-filter";
const url_run_workflow = "http://127.0.0.1:8000/run-workflow";

// HTML
// ヘッド
const Header = () => {
    const navigate = useNavigate();

    return (
        <div className="heading-container">
            <h1 onClick={() => navigate("/")}>Kami Go!</h1>
        </div>
    );
};

// java
// 絞り込み
export const handleFilterClick = async ({
    path,
    inputData = { data: [] },
    filterMode = null,
    filterType = "or",
    inputFilterIDs = [],
    inputText = "",
    sortKey = null,
    limitNumber = null,
    setQuery,
    setFilteredIDs,
    setFilteredDatas,
    navigate
}) => {
    const params = {
        filter_mode: filterMode,
        filter_type: filterType,
        input_filterIDs: inputFilterIDs,
        input_text: inputText,
        sort_key: sortKey,
        limit_number: limitNumber
    };

    // input_filterIDsが空でなかったらリストの中身を合体し、一つにする
    if (inputFilterIDs.length > 0) {
        params.input_filterIDs = inputFilterIDs.join(",");
    }

    try {
        // 「await」により非同期リクエストが完了するまで待機し、レスポンスを「res」に格納する
        const res = await axios.post(url_filter, inputData, { params });
        console.log("入力データ:", inputData);
        console.log("レスポンス全体:", res);
        console.log("レスポンスデータ部分:", res.data);

        setQuery(inputText);
        setFilteredIDs(inputFilterIDs);
        setFilteredDatas(res.data);

        // ページ遷移時にデータを渡す
        navigate(path, {
            state: {
                spotDatas: inputData,
                query: inputText,
                filteredIDs: inputFilterIDs,
                filteredDatas: res.data
            }
        });
    } catch (err) {
        console.error("エラーが発生しました:", err);
    }
};

export const selectMainSpot = ({
    path,
    inputData = { data: [] },
    spotData = null,
    setMainSpotID,
    navigate
}) => {
    setMainSpotID(spotData.spot_id)
    console.log("入力データ:", inputData);
    console.log("メインスポットID:", spotData.spot_id);
    navigate(path, {
        state: {
            spotDatas: inputData,
            mainSpotID: spotData.spot_id
        }
    });
}

export const handleMakePlanClick = async ({
    mainSpotID,
    inputData,
    filterType = "or",
    inputFilterIDs = [],
    inputTravelStart,
    inputTravelEnd
}) => {
    const params = {
        main_spotID: mainSpotID,
        filter_type: filterType,
        input_filterIDs: inputFilterIDs,
        input_travel_start: inputTravelStart,
        input_travel_end: inputTravelEnd
    };

    // input_filterIDsが空でなかったらリストの中身を合体し、一つにする
    if (inputFilterIDs.length > 0) {
        params.input_filterIDs = inputFilterIDs.join(",");
    }

    try {
        // 「await」により非同期リクエストが完了するまで待機し、レスポンスを「res」に格納する
        const res = await axios.post(url_run_workflow, inputData, { params });
        console.log("入力データ:", inputData);
        console.log("レスポンス全体:", res);
        console.log("レスポンスデータ部分:", res.data);
    } catch (err) {
        console.error("エラーが発生しました:", err);
    }
};

export default Header;
