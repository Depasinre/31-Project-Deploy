import './App.css'
import '@awsui/global-styles/index.css'

import AppLayout from '@awsui/components-react/app-layout'
import React from 'react'
import NavigateArea from './modules/NavigateArea/NavigateArea'
import {
  BrowserRouter,
  Routes,
  Route
} from 'react-router-dom'

import Overview from './Overview'
import Staff from './Staff'
import OrderHistory from './OrderHistory'
import Inventory from './Inventory'
import Customer from './Customer'

function App () {
  return (
    <AppLayout
      content={
        <BrowserRouter>
        <Routes>
          <Route exact path="/" element={<Overview/>}/>
          <Route exact path="/Staff" element={<Staff/>}/>
          <Route exact path="/OrderHistory" element={<OrderHistory/>} />
          <Route exact path="/Inventory" element={<Inventory/>}/>
          <Route exact path="/Customer" element={<Customer/>}/>
        </Routes>
        </BrowserRouter>
      }
      navigation={
        <NavigateArea> </NavigateArea>
      }
      toolsHide={true}
    />
  )
}

export default App
