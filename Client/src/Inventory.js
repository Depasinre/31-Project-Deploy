import '@awsui/global-styles/index.css'

import React from 'react'
import DisplayArea from '../src/modules/DisplayArea/DisplayArea'
import Header from '@awsui/components-react/header'

function Inventory (props) {
  return (
    <>
    <Header variant={'h1'}>Inventory</Header>
    <DisplayArea type = {'Inventory'}/>
    </>
  )
}

export default Inventory
