import React, { useState } from "react";
import Switch from "react-switch";
import Threads from "./Threads";
import darkmode from "../Assets/darkmode.svg";
const Home = () => {
  const [checked, setchecked] = useState(false);
  const [threads, setthreads] = useState(false);

  const handleClick = () => {
    if (checked) {
      setchecked(false);
    } else {
      setchecked(true);
    }
  };

  return (
    <div className="bg-[#333333] w-[100vw] h-[100vh]">
      {threads ? (
        <Threads />
      ) : (
        <div>
          <div className="flex justify-end p-4">
            <img src={darkmode} className="px-4" />
            <Switch
              onChange={handleClick}
              checked={checked}
              onColor={"#FFE600"}
              handleDiameter={30}
              uncheckedIcon={false}
              checkedIcon={false}
              boxShadow="0px 1px 5px rgba(0, 0, 0, 0.6)"
              activeBoxShadow="0px 0px 1px 10px rgba(0, 0, 0, 0.2)"
              height={20}
              width={48}
              className="react-switch"
              id="material-switch"
            />
          </div>
          <div className="mt-[22vh] flex flex-col mx-10 items-center justify-center">
            <h2 className="text-3xl text-white my-6 ">
              No Active Threads Found
            </h2>
            <button
              className="bg-[#222222]  rounded-2xl p-2 w-40 m-3 text-lg text-white"
              onClick={() => setthreads(true)}
            >
              Ask a Query !
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default Home;
