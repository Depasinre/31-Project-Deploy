import '@awsui/global-styles/index.css'
import React from 'react'
import SideNavigation from '@awsui/components-react/side-navigation'

function NavigateArea (props) {
  return (
    <SideNavigation
    header={{
      text: 'CSCE 310 Project: IKEA Storge',
      href: '/'
    }}
    items={[
      {
        text: 'Overview',
        type: 'link',
        href: '/'
      },
      {
        text: 'Staff',
        type: 'link',
        href: '/Staff'
      },
      {
        text: 'OrderHistory',
        type: 'link',
        href: '/OrderHistory'
      },
      {
        text: 'Inventory',
        type: 'link',
        href: '/Inventory'
      },
      {
        text: 'Customer',
        type: 'link',
        href: '/Customer'
      }]}
    />
  )
}

export default NavigateArea
