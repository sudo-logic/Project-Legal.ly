import React from "react";

const Input = ({ msg }) => {
  return (
    <div className="w-[70vw]">
      <div className="w-fit p-3 h-fit bg-[#494949]  rounded-lg text-center text-sm text-white rounded-bl-none align-right ml-[55vw]">
        {msg}
      </div>
    </div>
  );
};

export default Input;
