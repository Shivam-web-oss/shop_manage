import {  useEffect,useState } from "react";
function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetch("https://cuddly-palm-tree-7vv54jvxqwxpcx474-8000.app.github.dev")
      .then(res => res.json())
      .then(data => setMessage(data.message))
  },[]);
  return<h1>{message}</h1>
}

export default App;