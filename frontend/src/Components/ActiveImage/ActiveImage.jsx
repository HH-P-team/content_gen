import './ActiveImage.css';
import Progress from '../Progress/Progress';

export default function ActiveImage(props) {

    if (!props.data) {
        return (<Progress/>)
    }

    return (
        <img className="ActiveImage" src={"data:image/png;base64, " + props.data}/>
    );
}
