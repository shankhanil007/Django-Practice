import React from 'react'
import { useState, useEffect } from 'react';

export default function Message() {

    const [text, setText] = useState("Hello User");

    const changeMessage = () => {
        setText(["Thanks for subscribing"]);
    }

    return (
        <div>
            <h1>{text}</h1>
            <button onClick={() => changeMessage()}>Subscribe</button>
        </div>
    )
}
