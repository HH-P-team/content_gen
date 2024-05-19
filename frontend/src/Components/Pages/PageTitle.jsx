import './Subjects.css';

export default function PageTitle(props) {
    return (
        <div className='PageTitle'>
            <h2>{props.pageName}</h2>
        </div>
    );
}