import '@awsui/global-styles/index.css'

import React from 'react'
import DisplayArea from './modules/DisplayArea/DisplayArea'
import Header from '@awsui/components-react/header'

function Staff () {
  return (
    <>
    <Header variant={'h1'}>Staff</Header>
    <DisplayArea type = {'Staff'}/>
    </>
  )
}

export default Staff
