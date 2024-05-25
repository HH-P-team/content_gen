import './Button.css';
import * as React from 'react';
// import { Link } from 'react-router-dom';

export default function Button(props) {
    return (
        <button className="Button" disabled={props.disabled}>
            <div onClick={props.action}>{props.name}</div>
        </button>
    );
}