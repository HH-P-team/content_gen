import './Card.css';
import ActiveImage from '../ActiveImage/ActiveImage';
import { useEffect, useState } from 'react';
import toast from 'react-hot-toast';

export default function Card(props) {
    return (
        <div className="Card" data-id={props.id}>
            <div className='ImageWrapper'>
                <ActiveImage data={props.img}/>
            </div>
            <div>{props.name}</div>
        </div>
    );
}
