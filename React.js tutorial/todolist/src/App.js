import logo from './logo.svg';
import './App.css';
import Header from "./MyComponents/Header";
import Message from "./MyComponents/Message";
import ParentComponent from './MyComponents/ParentComponent'

function App() {
  return (
    <>
    {/* <Message /> */}
    <ParentComponent />
    </>
  );
}

export default App;
