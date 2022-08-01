import '@awsui/global-styles/index.css'
import React, { useState } from 'react'
import PropTypes from 'prop-types'

import Container from '@awsui/components-react/container'
import IdSearch from './submodules/IdSearch/IdSeardh'

function DisplayArea (props) {
  const [type] = useState(props.type)
  return (
    <Container>
        <IdSearch type = {type}/>
    </Container>
  )
}

DisplayArea.propTypes = {
  type: PropTypes.string
}
export default DisplayArea
