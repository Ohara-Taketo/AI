import React from 'react';
// 「BrowserRouter as Router」はルーティングの基盤を提供するコンポーネント「BrowserRouter」を「Router」という別名で用いるという意味
import {BrowserRouter as Router, Route, Link, Routes} from 'react-router-dom';

// ページのコンポーネント
import AItravel from './ai-travel';
import T001 from './T001';
import T002 from './T002';
import T003 from './T003';

function App() {
  return (
    <Router>
      <div>
        {/* 各ページへのルート設定 */}
        <Routes>
          {/* 「/」はデフォルトのURL */}
          {/* 「http://localhost:3000/」がデフォルト */}
          {/* 「element={<T001 />}」は指定したパスにアクセスしたときに表示するReactコンポーネントを指定する */}
          {/* 「element={<T001 />}」では「<T001 />」コンポーネント(T001.js)が表示される */}
          <Route path="/" element={<AItravel />} />
          <Route path="/T001" element={<T001 />} />
          <Route path="/T002" element={<T002 />} />
          <Route path="/T003" element={<T003 />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;