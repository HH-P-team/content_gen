import './MenuButton.css';
import * as React from 'react';
import { Link } from 'react-router-dom';

export default function MenuButton(props) {
    return (
        <button className="MenuButton">
            <Link className="ButtonLink" to={props.path}>{props.name}</Link>
        </button>
    );
}