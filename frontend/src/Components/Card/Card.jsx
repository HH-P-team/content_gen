import './Card.css';
import ActiveImage from '../ActiveImage/ActiveImage';

export default function Card(props) {
    return (
        <div className="Card">
            <div className='ImageWrapper'>
                <ActiveImage message={props.name}/>
            </div>
            <div>{props.name}</div>
        </div>
    );
}
