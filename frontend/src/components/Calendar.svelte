<script>
    import FullCalendar from 'svelte-fullcalendar';
    import dayGridPlugin from '@fullcalendar/daygrid';
    import timeGridPlugin from '@fullcalendar/timegrid';
    import interactionPlugin from '@fullcalendar/interaction'; // needed for dateClick
    let options = {
        dateClick: handleDateClick,
        droppable: true,
        editable: true,
        events: [
            { title: 'New Event', start: new Date() },
        ],
        initialView: 'dayGridMonth',
        plugins: [dayGridPlugin, timeGridPlugin, interactionPlugin],
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay',
        },
        height: 'auto',
        weekends: true,
    };
    let calendarComponentRef;
    let eventData = { title: 'my event', duration: '02:00' };


    function handleDateClick(event) {
        if (
            confirm('Would you like to add an event to ' + event.dateStr + ' ?')
        ) {
            const { events } = options;
            const calendarEvents = [
                ...events,
                {
                    title: 'Evento Cris puto',
                    start: event.date,
                    allDay: event.allDay,
                },
            ];
            options = {
                ...options,
                events: calendarEvents,
            };
        }
    }
</script>

<style>

    .demo-app-calendar {
        margin: 0 auto;
        width: 60%;
    }

</style>

<div class="demo-app">
    <div class="demo-app-calendar">
        <FullCalendar bind:this={calendarComponentRef} {options} />
    </div>
</div>