import React from "react";

const Input = ({ msg }) => {
  return (
    <div className="w-[70vw]">
      <div className="w-fit p-3 h-fit bg-[#494949] ml-auto rounded-lg text-center text-sm text-white rounded-br-none align-right ">
        {msg}
      </div>
    </div>
  );
};

export default Input;
