import Sidebar from "./Components/Sidebar";
import Home from "./Components/Home";
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
