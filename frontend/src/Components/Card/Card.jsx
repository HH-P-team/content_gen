import './Card.css';
import ActiveImage from '../ActiveImage/ActiveImage';

export default function Card(props) {
    console.log(props);
    return (
        <div className="Card" data-id={props.id}>
            <div className='ImageWrapper'>
                <ActiveImage message={props.name}/>
            </div>
            <div>{props.name}</div>
        </div>
    );
}
