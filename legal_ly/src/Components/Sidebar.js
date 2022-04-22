import React from "react";
import Logo from "../Assets/Logo.png";
import Declaration from "../Assets/Declaration.png";
import { Route, Link } from "react-router-dom";

function Sidebar() {
  return (
    <div className="bg-[#222222] w-[23vw] h-[100vh] text-white ">
      <div className="flex flex-col justify-between h-[98vh]">
        <img src={Logo} alt="Logo" className="w-[14vw] py-6  mx-auto" />
        <div className="flex flex-col justify-center  items-center">
          <button className="bg-[#333333] rounded-2xl p-2 w-32 my-3 text-lg">
            Threads
          </button>

          <button className="bg-[#333333] rounded-2xl p-2 w-32 m-3 text-lg">
            About Us
          </button>
        </div>
        <img src={Declaration} alt="Declaration" className="w-[15vw] mx-auto" />
      </div>
    </div>
  );
}

export default Sidebar;
