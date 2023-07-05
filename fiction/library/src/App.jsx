import React, { useState, useSyncExternalStore } from "react";
import Button from "./components/Books";
import Homescreen from "./components/Homescreen";

const App = () => {
  const [addBookForm, setAddBookForm] = useState(false);
  const handleClick = () => {
    console.log("Button clicked!");
  };
  return (
    <div>
      <h1>Welcome to the Fiction App</h1>
   
      <Homescreen />
    </div>
  );
};
export default App;
