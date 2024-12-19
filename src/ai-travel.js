import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import Header, { handleFilterClick } from "./template.js";

const AItravel = () => {
    const navigate = useNavigate();

    const url_getData = "http://127.0.0.1:8000/get-data";


    const [spotData, setSpotData] = useState(null);
    const [query, setQuery] = useState("");
    const [filteredIDs, setFilteredIDs] = useState([]); // 現在選択されているフィルタID
    const [filteredDatas, setFilteredDatas] = useState([]);

    const handleClick = async (
        path
    ) => {

        try {
            // 「await」により非同期リクエストが完了するまで待機し、レスポンスを「res」に格納する
            const res = await axios.get(url_getData);
            console.log("レスポンス全体:", res);
            console.log("レスポンスデータ部分:", res.data);

            handleFilterClick({
                path: path,
                inputData: res.data,
                sortKey: "KUT",
                limitNumber: 5,
                setQuery,
                setFilteredIDs,
                setFilteredDatas,
                navigate
            });
        } catch (err) {
            console.error("エラーが発生しました:", err);
        }
    };

    return (
        <div>
            {/* ヘッド */}
            {/* <div>はコンテンツ区分要素 */}
            <div>
                {/* onclick属性は、ユーザが要素をクリックした際に起動する処理を指定するイベント属性 */}
                {/* 「style = {{ cursor: "pointer"」を消したのでcssでcursor: pointer;とすること }} */}
                <h1 onClick={() => handleClick("/T001")}>AI</h1>
            </div>
        </div>
    );
};

export default AItravel;