import '@awsui/global-styles/index.css'

import React from 'react'
import DisplayArea from '../src/modules/DisplayArea/DisplayArea'
import Header from '@awsui/components-react/header'

function Overview (props) {
  return (
    <>
    <Header variant={'h1'}>Overview</Header>
    <DisplayArea type = {'Overview'}/>
    </>
  )
}

export default Overview
