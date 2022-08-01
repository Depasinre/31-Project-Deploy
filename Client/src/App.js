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
          <Route path="/Overview" element={<Overview/>}/>
          <Route path="/Staff" element={<Staff/>}/>
          <Route path="/OrderHistory" element={<OrderHistory/>} />
          <Route path="/Inventory" element={<Inventory/>}/>
          <Route path="/Customer" element={<Customer/>}/>
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
