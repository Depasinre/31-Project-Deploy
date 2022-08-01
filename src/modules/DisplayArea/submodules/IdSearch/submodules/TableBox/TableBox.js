import '@awsui/global-styles/index.css'
import React, { useState, useEffect } from 'react'
import PropTypes from 'prop-types'
import CollectionPreferences from '@awsui/components-react/collection-preferences'
import Pagination from '@awsui/components-react/pagination'
import Table from '@awsui/components-react/table'
import Container from '@awsui/components-react/container'
import Header from '@awsui/components-react/header'

function TableBox (props) {
  const [items, setItems] = useState(props.value)
  // const [type] = useState(props.type)

  const [itemsPerPage, setItemsPerPage] = useState(10)
  const [visibleFields, setVisibleFields] = useState(
    ['staID', 'staName', 'staJobTitle', 'staEmail']
  )
  const [start, setStart] = useState(1)

  useEffect(
    () => {
      console.log(props.value)
      setItems(props.value)
      console.log('items is ')
      console.log(items)
    }, [props.value]
  )
  /*
  let renderJSX
  const staffRenderJSX = 1
  if (type === 'Staff') {
    renderJSX = staffRenderJSX
  } */
  return (
    <Container>
    <Table
      header={<Header variant="h2">Staff</Header>}
      variant="container"
      preferences={
        <CollectionPreferences
          title="Preferences"
          visibleContentPreference={{
            title: 'Fields',
            options: [
              {
                options: [
                  { id: 'staID', label: 'Staff ID', editable: true },
                  {
                    id: 'staName',
                    label: 'Name'
                  },
                  {
                    id: 'staJobTitle',
                    label: 'Job'
                  },
                  {
                    id: 'staEmail',
                    label: 'Email'
                  }
                ]
              }
            ]
          }}
          pageSizePreference={{
            title: 'Items per page',
            options: [
              {
                value: 10,
                label: '10'
              },
              {
                value: 20,
                label: '20'
              },
              {
                value: 50,
                label: '50'
              }
            ]
          }}
          preferences={{
            pageSize: itemsPerPage,
            visibleContent: visibleFields
          }}
          onConfirm={(e) => {
            setItemsPerPage(e.detail.pageSize)
            setVisibleFields(e.detail.visibleContent)
          }}
          confirmLabel="Confirm"
          cancelLabel="Cancel"
        />
      }
      pagination={
        <Pagination
          ariaLabels={{
            nextPageLabel: 'Next page',
            previousPageLabel: 'Previous page',
            pageLabel: (pageNumber) => `Page ${pageNumber}`
          }}
          currentPageIndex={start}
          pagesCount={items.length / itemsPerPage}
          onChange={(e) => {
            setStart(e.detail.currentPageIndex)
          }}
          onNextPageClick={(e) => {
            setStart(e.detail.requestedPageIndex)
          }}
          onPreviousPageClick={(e) => {
            setStart(e.detail.requestedPageIndex)
          }}
        />
      }
      columnDefinitions={[
        {
          header: 'Staff ID',
          id: 'staID',
          cell: (item) => {
            return <p>{item.staID}</p>
          }
        },
        {
          header: 'Staff Name',
          id: 'staName',
          cell: (item) => {
            return <p>{item.staName}</p>
          }
        },
        {
          header: 'Job',
          id: 'staJobTitle',
          cell: (item) => {
            return <p>{item.staJobTitle}</p>
          }
        },
        {
          header: 'Email',
          id: 'staEmail',
          cell: (item) => {
            return <p>{item.staEmail}</p>
          }
        }
      ]}
      visibleColumns={visibleFields}
      items={items.slice(
        (start - 1) * itemsPerPage,
        start * itemsPerPage
      )}
    ></Table>
  </Container>

  )
}

TableBox.propTypes = {
  type: PropTypes.string,
  value: PropTypes.array
}

export default TableBox
