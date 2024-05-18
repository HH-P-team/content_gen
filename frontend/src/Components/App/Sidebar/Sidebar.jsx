import './Sidebar.css';
import Menu from '../../menu/Menu';
import logo from '../../../rt_logo.png'

export default function Sidebar() {
    return (
        <aside className="App-sidebar">
            <img className='Img' src={logo} alt='logo'/>
            <Menu />
        </aside>
    );
}
