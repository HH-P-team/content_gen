import './PageHeader.css';
import PageTitle from './PageTitle';

export default function PageHeader(props) {
    return (
        <div className='PageHeader'>
            <PageTitle pageName={props.pageName}/>
            {props.controlElement}
        </div>
    );
}
