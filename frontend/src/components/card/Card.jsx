import './Card.css';

import ImageWrapper from './ImageWrapper';

export default function Card(props) {
    return (
        <div className="Card">
            <ImageWrapper message={props.name}/>
            <div>{props.name}</div>
        </div>
    );
}
