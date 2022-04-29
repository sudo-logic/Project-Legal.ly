import React from "react";
import axios from "axios";

const Response = ({ msg }) => {
  const formMsg = new FormData();

  // formMsg.append("msg", msg);
  // axios({
  //   method: "post",
  //   url: "http://10.5.133.8:5000/api",
  //   headers: { "Content-Type": "multipart/form-data" },
  //   data: formMsg,
  // }).then((response) => {
  //   console.log(response);
  // });

  return (
    <div className="p-3 ">
      <div className="h-fit rounded-lg mt-2 text-sm text-white rounded-bl-none bg-[#222222] p-3 w-fit ml-0">
        {msg}
      </div>
    </div>
  );
};

export default Response;
