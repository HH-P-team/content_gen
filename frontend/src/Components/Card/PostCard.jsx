import './PostCard.css';
import ActiveImage from '../ActiveImage/ActiveImage';
import { useEffect, useState } from 'react';
import toast from 'react-hot-toast';

export default function PostCard(props) {
    return (
        <div className="PostCard" data-id={props.id}>
            <div className="PostCardHeader">{props.name}</div>
            <div className="PostCardContainer">
                <div className='PostCardSection'>
                    <div className='ImageWrapperPost'>
                        <ActiveImage data={props.img}/>
                    </div>
                </div>
                <div className='PostCardSection'>
                    {props.description}
                </div>
            </div>
        </div>
    );
}
