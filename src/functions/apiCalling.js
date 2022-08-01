import axios from 'axios'

const fakeDatabase = [
  // stuff 1
  [
    {
      staID: '0',
      staName: 'John',
      staJobTitle: 'Manager',
      staEmail: 'john@gmail.com'
    },
    {
      staID: '1',
      staName: 'Jack',
      staJobTitle: 'Employee',
      staEmail: 'jack@gmail.com'
    }
  ]
]

function storeIDToStatistics (storeID) {
  console.log('API calling....')
  axios.post('http://127.0.0.1:8000/readStaffbyID', { storeID })
    .then(function (response) {
      alert(response.data)
    })
    .catch(function (error) {
      alert(error)
    })
}

function fakeStaffAPICall (storeID) {
  if (storeID === 1) {
    return fakeDatabase[0]
  }
}

export {
  storeIDToStatistics,
  fakeStaffAPICall
}
