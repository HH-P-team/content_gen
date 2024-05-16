import './Card.css';

export default function Card(props) {
    return (
        <div className="Card">
            <div className='ImageWrapper'></div>
            <div>{props.name}</div>
        </div>
    );
}
