import React from 'react'
import ChildComponent from './ChildComponent'

const ParentComponent = (props) => {

  const greetParent = (childName) => { 
    alert(`Hello Parent from ${childName}`)
  }

  return (
    <div>
      <ChildComponent greetHandler={greetParent} />
    </div>
  )
}

export default ParentComponent
