import React from "react";
import axios from "axios";

const Response = ({ msg }) => {
  const formMsg = new FormData();
  console.log(msg);
  formMsg.append("msg", msg);
  axios({
    method: "post",
    url: "10.5.133.8:5000/api",
    data: formMsg,
  }).then((response) => {
    console.log(response);
  });

  return (
    <div className="p-3 ">
      <div className="h-fit rounded-lg mt-2 text-sm text-white rounded-bl-none bg-[#222222] p-3 w-fit">
        Hello there !
      </div>
    </div>
  );
};

export default Response;
