import '@awsui/global-styles/index.css'

import React from 'react'
import DisplayArea from '../src/modules/DisplayArea/DisplayArea'
import Header from '@awsui/components-react/header'

function OrderHistory (props) {
  return (
    <>
    <Header variant={'h1'}>Order History</Header>
    <DisplayArea type = {'OrderHistory'}/>
    </>
  )
}

export default OrderHistory
