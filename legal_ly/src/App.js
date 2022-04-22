import Sidebar from "./Components/Sidebar";
import Home from "./Components/Home";
import Threads from "./Components/Threads";
import { BrowswerRouter, Routes, Route } from "react-router-dom";
function App() {
  return (
    <div className="App">
      <div className="font-[Poppins] flex">
        <Sidebar />
        <Home />
      </div>
    </div>
  );
}

export default App;
