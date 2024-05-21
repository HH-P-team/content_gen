import './Card.css';
import ActiveImage from '../ActiveImage/ActiveImage';
import { useEffect, useState } from 'react';

export default function Card(props) {

    const [data, setData] = useState('');

    useEffect(() => {
        props.request(props.params).then((data) => {
            if (data.status) {
                setData(data.result);
            }
        });
    }, []);
    
    return (
        <div className="Card" data-id={props.id}>
            <div className='ImageWrapper'>
                <ActiveImage data={data}/>
            </div>
            <div>{props.name}</div>
        </div>
    );
}
