import '@awsui/global-styles/index.css'
import PropTypes from 'prop-types'
import Input from '@awsui/components-react/input'
import ColumnLayout from '@awsui/components-react/column-layout'
import React, { useEffect, useState } from 'react'
import Button from '@awsui/components-react/button'
import FormField from '@awsui/components-react/form-field'
import { fakeStaffAPICall, storeIDToStatistics } from '../../../../functions/apiCalling'

import TableBox from './submodules/TableBox/TableBox'

function IdSearch (props) {
  const initialStaff = [{
    staID: '',
    staName: '',
    staJobTitle: '',
    staEmail: ''
  }]
  const [storeIdInput, setStoreIdInput] = useState() // The user inputt value in the search bar
  const [type] = useState(props.type)
  const [fetchedValue, setFetchedValue] = useState(initialStaff)
  // functons
  function onInputChange (e) {
    setStoreIdInput(e.detail.value)
  }

  function searchButtonClick (e) {
    if (type === 'Staff') {
      setFetchedValue(fakeStaffAPICall(parseInt(storeIdInput)))
      storeIDToStatistics(parseInt(storeIdInput))
    }
  }
  useEffect(
    () => {
      console.log('fetched data is')
      console.log(fetchedValue)
    }, [fetchedValue]
  )
  return (
    <>
        <ColumnLayout columns = {3}>
            <FormField
            Lable={'Store ID'}>
            <Input
                id={'inputbar'}
                type ={'number'}
                placeholder={'Enter your store ID'}
                onChange={onInputChange}
                value ={storeIdInput}
            />
            <Button iconName={'search'}
                    onClick={searchButtonClick}>
            Search</Button>
            </FormField>
        </ColumnLayout>
        <TableBox type = {'Staff'} value = {fetchedValue}></TableBox>

    </>
  )
}

IdSearch.propTypes = {
  type: PropTypes.string
}

export default IdSearch
