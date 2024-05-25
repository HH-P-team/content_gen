import './ActiveImage.css';

export default function ActiveImage(props) {
    return (
        <img 
            className="ActiveImage"
            src={`http://localhost:8000/product_images/${props.data ? props.data.uuid : 'trololo'}.jpg`}
        />
    );
}
