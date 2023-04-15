import './App.css'
import Home from './pages/Home'
import Dashboard from './pages/Dashboard'
import testData from './assets/testData.json'

import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";


const router = createBrowserRouter([
  {
    path: "/",
    element: <Home />,
  },
  {
    path: "/dashboard",
    element: <Dashboard data={testData}/>,
  }
]);


function App() {
  return (
    <div className="App">
      <RouterProvider router={router} />
    </div>
  )
}

export default App
