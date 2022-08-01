import '@awsui/global-styles/index.css'

import React from 'react'
import DisplayArea from '../src/modules/DisplayArea/DisplayArea'
import Header from '@awsui/components-react/header'

function Customer (props) {
  return (
    <>
    <Header variant={'h1'}>Customer</Header>
    <DisplayArea type = {'Customer'}/>
    </>
  )
}

export default Customer
